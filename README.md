# Word-Cloud

A word (or Tag) cloud is a visual representation for text data, typically used to depict keyword metadata (tags) on websites, 
or to visualize free form text. Tags are usually single words, and the importance of each tag is shown with font size or colour. 
This format is useful for quickly perceiving the most prominent terms and for locating a term to determine its relative prominence. We are going to use Abraham Lincoln's Gettysburg Address of 1863, which you will have already seen. This is famous for many things, including for being a short speech.
We are going to construct a simple web page. Each word will be enclosed in span tags and will have its individual font size set.

As this is not an exercise in HTML creation, the text of the HTML page is provided (see link below):

<!DOCTYPE html>
<html>
<head lang="en">
<meta charset="UTF-8">
<title>Tag Cloud Generator</title>
</head>
<body>
<div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">

<!--Your SPAN elements should be inserted here-->

</div>
</body>
</html>

The format of a span element is <span style="font-size: XXpx"> WORD </span>. Where XX is the size in pixels and WORD is the word 
being represented.
Tasks

You will need to do some simple analysis on the speech to complete this exercise including counting the number of occurrences 
of each word. You should then create the completed HTML page and write it an a .html file to your local cache. You can open this file in PyCharm and test it using a browser of your choice from within the editor window.
Some hints

    Import the string module. This gives string.whitespace, a string containing all of the white space characters and string.
    punctuation, a string containing all of the punctuation characters.

    Ignore words of three characters or less. These are not likely to be significant.
    When your file has been created, open this in PyCharm. A set of icons will appear offering browser choices to render 
    the page. You may use a browser to render your page but for no other reason except to submit via Webcourses.

Data

The files are on http://193.1.33.31:88/pa1/gettysburg.txt and http://193.1.33.31:88/pa1/stopwords.txt

There is a sample HTML file on http://193.1.33.31:88/pa1/tagcloud.html. This contains the same text as the example on this page. You can use the text of this in your program.
