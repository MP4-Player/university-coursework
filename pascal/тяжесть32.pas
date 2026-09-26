function numProg( start, x: real ): integer;
var K: integer;
begin
  if x < start then numProg := 0
  else if x = start then numProg := 1
  else 
    numProg := numProg(start+1,x) + numProg(start+1.5,x);
end;

begin
 writeln( numProg(7,20) );
end.