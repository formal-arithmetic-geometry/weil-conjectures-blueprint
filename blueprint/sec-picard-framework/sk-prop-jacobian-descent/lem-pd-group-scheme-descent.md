+++
id = "lem-pd-group-scheme-descent"
kind = "lemma"
title = "The descended scheme is a group scheme"
lean = ["CategoryTheory.Over.DescentDatum.existsUnique_grpObj_of_isPullback", "CategoryTheory.Over.DescentDatum.exists_commGrpObj_of_isPullback"]
order = 872
uses = ["def-pc-base-change", "def-pd-descent-datum", "def-sc-group-scheme", "lem-pd-morphisms-descend"]
+++
Let $k\subseteq K$ be a finite separable field extension, let $J_K$ be a scheme
over $K$ with a descent datum over
$\Spec(K)/\Spec(k)$ which is effective with descended scheme $J$, and suppose
that $J_K$ carries a $K$-group scheme structure
whose multiplication, unit and inverse are compatible with the descent datum.
Then $J$ carries a unique $k$-group scheme structure whose
base change to $K$ is the given one.
