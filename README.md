<p align="center">
  <img src="https://github.com/serhatdog/enchanted-words/blob/main/enchantedwords_logo.png?raw=true" alt="Enchanted Words">
</p>

<p align="center"><b>Author: Serhat Dogan</b><p>
<p align="center"><b>Last update: 18.08.2022</b><p>
<p align="center"><b>Preparing...</b><p>
  
<h1 align="center">What is Enchanted Words?</h1>

Enchanted Words is a method that allows your brain to recognize the word completely without reading it and thus read it faster by fading the words at a certain rate by processing on a string that you translated from a file or sent directly by yourself. The data is first saved as html, then converted to a pdf file and presented to the reader in the final. It is still in the development stage and there are many disadvantages, but I am thinking of improving it by adding performance improvements and different mathematical methods in the future.

<p align="center">
  <img src="https://github.com/serhatdog/enchanted-words/blob/main/example_output.png?raw=true" alt="Enchanted Words">
</p>

**How to create a pdf file like this?**

    import enchantedwords
    
    text = open("your-text-file.txt", 'r', encoding = "utf-8").read()   #you can read text from the file
    or
    text = "Hello Github!"                                              #or you can just write by yourself
    
    enchantedwords.enchant(text, "Title")
    
All done, you just create your first pdf with using this method!
