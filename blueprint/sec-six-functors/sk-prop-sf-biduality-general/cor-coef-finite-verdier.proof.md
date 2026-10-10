+++
kind  = "proof"
of    = "cor-coef-finite-verdier"
+++
Apply [thm-coef-finite-hom] with second argument
$\omega_{X,A}$, and then use
[lem-coef-finite-dualizing] on that argument. The resulting
map is $d_{K,A,B}$. Evaluation compatibility follows from
the two comparisons already proved, and transposing evaluation
as in [lem-weil-duality-pairing] gives double-dual
compatibility. The cocycle is their quotient cocycle. The Tor
bound is [lem-weil-verdier-preservation-strata], together
with preservation of the Tor interval by scalar extension.
