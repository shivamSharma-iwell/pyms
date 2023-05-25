from flask import Flask, request
from controllers import controller

app = Flask(__name__)

@app.route('/pythonDownloadInvoice', methods=['POST'])
def downloadInvoice():
    result = controller.downloadInvoiceController(request.data)
    return result

if __name__=="__main__":
    app.run(host="localhost", port=8000, debug=True)
