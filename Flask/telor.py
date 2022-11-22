import cv2
from flask import Flask
from flask import url_for, render_template, request


app = Flask(__name__)

def ini_apa_sih(path):    
    #test_image = image.load_img(path, target_size = (64, 64))
    #test_image = image.img_to_array(test_image)
    #test_image = np.expand_dims(test_image, axis = 0)

    #result = classifier.predict_classes(test_image)
    
    return 'lol'

@app.route('/')
def hello_world():
  return render_template('halo.html')

@app.route('/ini_apa_upload', methods = ['GET', 'POST'])
def ini_apa_upload():
   if request.method == 'POST':
      f = request.files['file']
      path = './static/images' + url_for('hello_world') + '_' + f.filename
      path_gray = './static/imagesgray' + url_for('hello_world') + '_' + f.filename
      path_ini = 'static/images' + url_for('hello_world') + '_' + f.filename
      f.save(path)
      image = cv2.imread(path)
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      cv2.imwrite(path_gray,gray)

      #return path
      nama_ini = ini_apa_sih(path)
      
      return render_template(
        'hasil_prediksi.html',
        ini = "wkwk",
        posisi = path_gray
      )