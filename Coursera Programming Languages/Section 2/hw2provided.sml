(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

fun all_except_option (x, xs) =
    let fun f (xs) = 
	    case xs of
		[] => []
	      | i::xs' => 
		if same_string(i,x)
		then xs'
		else i::f(xs')
	val rs = f(xs)
    in
	if rs = xs
	then NONE
	else SOME rs
    end

fun get_substitutions1 (sLL, s) =
    case sLL of
	[] => []
     | sL::sLL' => 
       case all_except_option(s,sL) of
	   NONE => get_substitutions1(sLL',s)
	 | SOME xs => xs @ get_substitutions1(sLL',s)

fun get_substitutions2 (sLL, s) = 
    let fun aux (sLL, acc) =
	    case sLL of
		[] => acc
	     | sL::sLL' =>
	       case all_except_option (s,sL) of
		   NONE => aux(sLL',acc)
		 | SOME x => aux(sLL',x @ acc)
    in aux(sLL, [])
    end

fun similar_names (sLL, fullName) =
    let
	val {first=f,middle=m,last=l} = fullName
	val names = get_substitutions2(sLL,f)
	fun aux (ns,acc) =
	    case ns of
		[] => acc
	      | n'::ns' =>aux(ns',{first=n',middle=m,last=l}::acc)
    in
	aux(names,[fullName])
    end
	    
(* you may assume that Num is always used with values 2, 3, ..., 9
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

(* put your solutions for problem 2 here *)

fun card_color card =
    case card of
	(Clubs,rank) => Black
      | (Spades,rank) => Black
      | (Hearts,rank) => Red
      | (Diamonds,rank) => Red

fun card_value card = 
    case card of
	(suit,Ace) => 11
     | (suit,King) => 10
     | (suit,Queen) => 10
     | (suit,Jack) => 10		   
     | (suit,Num(x)) => x

fun remove_card (cards, c, e) =
    let
	fun append (xs,ys) =
	    case xs of
		[] => ys
	      | x::xs' => if x = c
			  then xs'
			  else append(xs',ys@[x]) 
	val rs = append(cards,[])
    in
	if rs = cards
	then raise e
	else rs
    end

fun all_same_color (cs) =
    case cs of
	[] => true
     | _::[] => true
     | c1::(c2::cs') => card_color(c1) =  card_color(c2) andalso all_same_color(cs')


fun sum_cards (cs) =
    let fun f(cs,acc) =
	    case cs of 
		[] => acc
	      | c::cs' => f(cs',acc+card_value(c))
    in 
	f(cs,0)
    end

fun score (cs,goal) =
    let val sum = sum_cards(cs)
	val pScore = if sum > goal
		     then (sum-goal) * 3
		     else goal - sum
    in 
	if all_same_color(cs)
	then pScore div 2
	else pScore
    end	    

fun officiate (cs,ms,goal) =
    let
	exception IllegalMove
	fun game (cs,ms,held) =
	    case sum_cards(held)>goal of
		true => held
	     | false => 
	       case ms of
		   [] => held
		 | Discard card::ms' => 
		   game(cs,ms',remove_card(held,card,IllegalMove))
		 | Draw::ms' => 
		   case cs of
		       [] => held
		     | c::cs' => game(cs',ms', c::held)
    in
	score(game(cs,ms,[]),goal)
    end
