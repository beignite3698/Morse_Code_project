from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def get_data():
    return render_template('data.html')

@app.route('/home')
def home():
    home=request.args.get('q')
    my_string=home 
    return new_data(my_string)
    
def new_data(my_string):
    my_string=my_string.upper()
    
    mean={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'}
       
    response=''
    for i in my_string: #ab
        if(i==' '):
            response=response+' / '
        
        if(i in mean):       
            response=response+mean[i]      
    return response  
        
    
    
    
    
if __name__=="__main__":
    app.run(port=89)
    
    
