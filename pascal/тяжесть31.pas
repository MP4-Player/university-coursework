function numProg( start, x: integer ): integer;
var K: integer;
begin
  if x < start then numProg := 0
  else if x = start then numProg := 1
  else 
    numProg := numProg(start+2,x) + numProg(start*3,x);
end;

begin
 writeln( numProg(1,55) );
end.