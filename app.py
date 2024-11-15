from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        angkabiner = request.form.get('angkabiner')  

        operation = request.form.get('operation')
        
        try:
            angkabiner = int(angkabiner)
            hasil = []
            hasilplus = 0
            intoarray = [int(digit) for digit in str(angkabiner)]
            pangkat = len(intoarray) - 1
            #cek bilangan biner atau tidak
            cek_dengan_kali = 1
            if operation == 'b2d':
                result = intoarray
                for i in range(0, len(intoarray)):
                    hasiloperasi = intoarray[i] * 2 ** pangkat
                    hasil.append(hasiloperasi)
                    pangkat -= 1
                                    
                for i in range(0, len(intoarray)):
                    hasilplus += hasil[i]
                    
                for i in range(0,len(intoarray)):
                    cek_dengan_kali *= intoarray[i]
                
                if cek_dengan_kali > 1:
                    result = "Angka tersebut bukanlah bilangan biner"
                else:
                    result = hasilplus


            else:   
                result = "Operasi tidak valid"
        except ValueError:
            result = "Input tidak valid"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
