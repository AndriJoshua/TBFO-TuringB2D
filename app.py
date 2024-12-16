from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Fungsi Mesin Turing untuk Konversi Biner ke Desimal
def turing_b2d(angkabiner):
    tape = list(angkabiner)
    head = 0
    state = "START"
    result = 0
    pangkat = len(tape) - 1

    while state != "Final_state":
        symbol = tape[head]

        if state == "START":
            if symbol == '0' or symbol == '1':
                result += int(symbol) * (2 ** pangkat)
                pangkat -= 1
                head += 1
                if head >= len(tape):
                    state = "Final_state"
            else:
                return {"error": "Tape mengandung angka non-biner."} 

    return {"result": result}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        angkabiner = request.form.get('angkabiner')
        operation = request.form.get('operation')

        if operation == 'b2d':
            # Validasi input
            if not angkabiner or not all(ch in '01' for ch in angkabiner):
                return jsonify({"error": "Tape mengandung angka non-biner."}), 400
            
            result = turing_b2d(angkabiner)
            if "error" in result:
                return jsonify(result), 400  # Mengembalikan pesan error(kalau ada)
            return jsonify(result)  # hasil dikembalikan dengan json
        else:
            return jsonify({"error": "Operasi tidak valid."}), 400

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
