from email import message
from unicodedata import category
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__) 
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    title = 'Superstore Profit Prediction'
    return render_template('home3.html', title=title)


@app.route('/predict', methods=['POST'])
def predict():
    Segment_Corporate=0
    Segment_HomeOffice=0
    Category_OfficeSupplies=0
    Category_Technology=0
    Category_Furniture=0
    requests = [ str(x) for x in request.form.values()]
    print(list(request.form.values()))

    sales = float(request.values['sales'])
    Discount = float(request.values['discount'])
    shipping_cost = float(request.values['shipping'])
    Quantity = float(request.values['quantity'])
    
    Segment_Consumer= request.form['Segment_Consumer']
    if(Segment_Consumer=='Consumer'):
        Segment_Consumer=1
        Segment_Corporate=0
        Segment_HomeOffice=0
    elif(Segment_Corporate=='Corporate'):
        Segment_Consumer=0
        Segment_Corporate=1
        Segment_HomeOffice=0
    else:
        Segment_Consumer=0
        Segment_Corporate=0
        Segment_HomeOffice=1
            
    category= request.form['Category_Furniture']
    if(Category_Furniture=='Furniture'):
        Category_Furniture=1
        Category_OfficeSupplies=0
        Category_Technology=0
    elif(Category_OfficeSupplies=='Office Supplies'):
        Category_Furniture=0
        Category_OfficeSupplies=1
        Category_Technology=0
    else:
        Category_Furniture	=0
        Category_OfficeSuppliese=0
        Category_Technology=1


    input_data = np.array([[sales,Discount,shipping_cost,Quantity,Segment_Consumer,Segment_Corporate,Segment_HomeOffice,
    Category_Furniture,Category_OfficeSupplies,Category_Technology]])
   
    output=model.predict(input_data)
    output=output.item()
    return render_template ('result.html',prediction_text="The profit is .{}".format(output))

    # prediction = np.array([[segment,region,ship_mode]])
    # output=model.predict(prediction)
    # print(prediction)
    # output=output.item()
    # if output == 0:
    #    return render_template ('home1.html',prediction_text="profit")
    # else:
    #    return render_template ('home1.html',prediction_text="loss")
    
    # # return render_template ('home1.html',message="hello" )

if __name__=='__main__':
    app.run(host="0.0.0.0", port=9090, debug=True)