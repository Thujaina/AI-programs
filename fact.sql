--factorial of a number

CREATE OR REPLACE PROCEDURE sum_fibonacci(n IN NUMBER)
IS
  a NUMBER := 0;
  b NUMBER := 1;
  next NUMBER;
  total NUMBER := 0;
  i NUMBER := 1;
BEGIN
  WHILE i <= n LOOP
    total := total + a;
    next := a + b;
    a := b;
    b := next;
    i := i + 1;
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('Sum of first ' || n || ' Fibonacci numbers is: ' || total);
END;
/
-- Execution
EXEC sum_fibonacci(7);  -- 0+1+1+2+3+5+8 = 20
