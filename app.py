from flask import Flask, request, render_template

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
                
                return "Tape mengandung angka non-biner."

    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        angkabiner = request.form.get('angkabiner')  
        operation = request.form.get('operation')

        if operation == 'b2d':
            if angkabiner.isdigit():
                result = turing_b2d(angkabiner)
            else:
                result = "Input tidak valid. Masukkan angka biner."

        else:
            result = "Operasi tidak valid"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
