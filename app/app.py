import os
import cv2
from flask import Flask, render_template, request, jsonify
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
from skimage import io

INDEX = os.path.join(os.path.dirname(__file__), 'index.csv')

# create flask instance
app = Flask(__name__)


# main route
@app.route('/')
def index():
	return render_template('index.html')

# search route
@app.route('/search', methods=['POST'])
def search():

	if request.method == "POST":

		RESULTS_ARRAY = []

		# get url
		image_url = request.form.get('img')

		try:

			# initialize the image descriptor
			cd = ColorDescriptor((8, 12, 3))

			# load the query image and describe it
			query = io.imread(image_url)

			query = (query * 255).astype("uint8")
			(r, g, b) = cv2.split(query)
			query = cv2.merge([b, g, r])
			features = cd.describe(query)


			# perform the search
			searcher = Searcher(INDEX)
			results = searcher.search(features)

			# loop over the results, displaying the score and image name
			for (score, resultID) in results:
				RESULTS_ARRAY.append(
					{"image": str(resultID), "score": str(score)})


			# return success
			return jsonify(results=(RESULTS_ARRAY[::-1][:3]))

		except:

			# return error
			return (jsonify({"sorry": "Sorry, no results! Please try again."}), 500)


# run!
if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)