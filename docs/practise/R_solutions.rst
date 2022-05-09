##############
R Solutions
##############

#. Imagine rolling a fair, six-sided die, and then flipping a fair, two-sided coin the number of times specified with
the die (i.e., if we roll a 3, flip the coin 3 times). Let X be the number of heads you get in this experiment.
Use a simulation in R to estimate the mean, median and mode of X.

.. code-block:: r

    #replicate
    set.seed(110)
    sims = 1000

    #keep track of X
    X = rep(0, sims)


    #run the loop
    for(i in 1:sims){

      #generate a roll
      roll = sample(1:6, 1)

      #flip the coin the specified number of times
      for(j in 1:roll){

        #flip the coin
        #recall that 'runif(1)' draws a random value between 0 and 1, so
        #   count 'heads' as getting a value below 1/2
        flip = runif(1)

        #see if we got heads; increment if we did
        if(flip <= 1/2){
          X[i] = X[i] + 1
        }
      }
    }

    #find the mean and median
    mean(X); median(X)

The default highlighting language is Python:
it can be be changed using the ``highlight`` directive
within a document::

   .. highlight:: html

   The literal blocks are now highlighted as HTML, until a new directive is found.

   ::
      <html><head></head>
      <body>This is a text.</body>
      </html>

   The following directive changes the hightlight language to SQL.

   .. highlight:: sql

   ::
      SELECT * FROM mytable

   .. highlight:: none

   From here on no highlighting will be done.

   ::
      SELECT * FROM mytable



.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'