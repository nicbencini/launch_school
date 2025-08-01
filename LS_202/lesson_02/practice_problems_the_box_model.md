## Question 1

1. Given the code below, what is the minimum width and height (in pixels) that the `div` needs to entirely contain the `img` element (including its margins)?

   Copy Code

   ```html
   <div>
     <img src="#" alt="test">
   </div>
   ```

   Copy Code

   ```css
   div {
     background-color: lightgray;
     border: 1px solid black;
     box-sizing: border-box;
     display: inline-block;
     margin: 0;
     padding: 0;
   }
   
   img {
     border: 4px solid red;
     box-sizing: content-box;
     display: inline-block;
     height: 300px;
     margin: 20px 19px 10px 11px;
     padding: 10px 20px;
     width: 500px;
   }
   ```

   Answer

   width = 500 + 4 + 4 + 19 + 11 + 20 + 20 + 1 + 1= 580

   height = 300 + 4 + 4 + 20 + 10 + 10 + 10 + 1 + 1 = 360
   
   ## Question 2
   
   Given the code below, what is the minimum width and height (in pixels) that the `div` needs to entirely contain the `section` element (including its margins)? How does this differ from the result of the previous practice problem?
   
   ```html
   <div>
     <section>content</section>
   </div>
   ```
   
   ```css
   div {
     background-color: lightgray;
     border: 1px solid black;
     box-sizing: border-box;
     display: inline-block;
     margin: 0;
     padding: 0;
   }
   
   section {
     border: 4px solid red;
     box-sizing: content-box;
     display: block;
     height: 300px;
     margin: 20px 19px 10px 11px;
     padding: 10px 20px;
     width: 500px;
   }
   ```
   
   Width = 500 + 20 + 20 + 19 + 11
   
   ## Question 3
   
   Given the code below, what is the minimum width and height (in pixels) that the `div` needs to entirely contain the `em` element (including its margins)?
   
   Copy Code
   
   ```html
   <div>
     <em>content</em>
   </div>
   ```
   
   Copy Code
   
   ```css
   div {
     background-color: lightgray;
     border: 1px solid black;
     box-sizing: border-box;
     display: inline-block;
     margin: 0;
     padding: 0;
   }
   
   em {
     border: 4px solid red;
     box-sizing: content-box;
     display: inline;
     height: 300px;
     margin: 20px 19px 10px 11px;
     padding: 10px 20px;
     width: 500px;
   }
   ```





