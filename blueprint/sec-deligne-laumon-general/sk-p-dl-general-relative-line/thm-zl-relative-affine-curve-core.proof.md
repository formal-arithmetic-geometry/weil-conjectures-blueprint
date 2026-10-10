+++
kind  = "proof"
of    = "thm-zl-relative-affine-curve-core"
uses = ["lem-zl-mixed-punctual-cutoff", "lem-zl-relative-curve-mixedness", "lem-zl-relative-curve-punctual"]
+++
By [lem-zl-relative-curve-punctual], all local Frobenius
eigenvalues on $R^ih_!\mathcal F$ have absolute value at most
$q_y^{(w+i)/2}$. The curve-reduction lemma [lem-zl-relative-curve-mixedness]
supplies a finite mixed filtration of this sheaf. Apply
[lem-zl-mixed-punctual-cutoff] with $v=w+i$.
This proves the bound without assuming that unrelated filtrations
of the individual stalks glue to Weil subsheaves.
