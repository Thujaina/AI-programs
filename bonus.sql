--bonus calculation

CREATE OR REPLACE PROCEDURE calc_bonus(fid_in IN NUMBER)
IS
  sal faculty.salary%TYPE;
  bonus NUMBER;
BEGIN
  SELECT salary INTO sal
  FROM faculty
  WHERE fid = fid_in;

  IF sal > 20000 THEN
    bonus := sal * 0.2;
  ELSIF sal BETWEEN 10001 AND 20000 THEN
    bonus := sal * 0.1;
  ELSE
    bonus := sal * 0.05;
  END IF;

  DBMS_OUTPUT.PUT_LINE('Bonus = ' || bonus);
END;
/
-- Execution
EXEC calc_bonus(101);
