CREATE OR REPLACE PROCEDURE single_digit_sum(n IN NUMBER)
IS
  digit NUMBER;
  total NUMBER := n;
BEGIN
  WHILE total >= 10 LOOP
    digit := total;
    total := 0;
    WHILE digit > 0 LOOP
      total := total + MOD(digit, 10);
      digit := TRUNC(digit / 10);
    END LOOP;
  END LOOP;
  DBMS_OUTPUT.PUT_LINE('Repeated digit sum: ' || total);
END;
/
-- Execution
EXEC single_digit_sum(9875);  -- 9+8+7+5 = 29, then 2+9 = 11, then 1+1 = 2
