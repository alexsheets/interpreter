(define (fac n)
  (define (f g n x)
    (if (= n 0) x
        (g g (- n 1) (* n x))))
  (f f n 1))
