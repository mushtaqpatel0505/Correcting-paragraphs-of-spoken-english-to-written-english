# Correcting-paragraphs-of-spoken-english-to-written-english
Created a reusable library that can convert a paragraph of spoken english to written english. For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

# Installation:
Please ensure that you have pip3, spacy and, word2number, before installing spoken_to_written_correction

You can install the module using Python Package Index using the below command.

  >>python3 setup.py install

# Usage:

  >>python3
  
  >>from spoken_to_written_correction import correction
  
  >>correction.main()
   
    Enter the paragraph: I am a M L engineer. I completed my aganitha assignment today at 12 P M. They are giving three hundred fifty       dollars per month as stipend. The agaaanitha word contain triple a in it. 
    ---------------------------------------------------
    Corrected paragraph
    I am a ML engineer. I completed my aganitha assignment today at 12 PM. They are giving $350 per month as stipend. The agaaanitha         word contain aaa in it. 


# Bugs/Errors

If you find any bugs/errors in the usage of above code, please raise an issue through Github.

# License

MIT License

Copyright (c) 2019 Mushtaq Patel Github

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# Future Work

- correction of date

- punctuation correction
 
