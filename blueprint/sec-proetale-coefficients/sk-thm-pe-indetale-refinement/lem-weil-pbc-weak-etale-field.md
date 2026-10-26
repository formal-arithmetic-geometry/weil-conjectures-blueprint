+++
id = "lem-weil-pbc-weak-etale-field"
kind = "lemma"
title = "Weakly etale algebras over a field"
order = 915
lean = ["Algebra.WeaklyEtale.etale_of_fg", "Algebra.Etale.iff_exists_algEquiv_prod", "Algebra.WeaklyEtale.indEtale_field", "Ring.AbsolutelyFlat.of_flat_lmul'", "Algebra.WeaklyEtale.isSeparable_residueField"]
uses = ["def-weil-pbc-ind-etale-algebra", "lem-weil-pbc-ind-etale-stability", "lem-weil-pbc-weak-etale-tor"]
+++
If $k$ is a field and $B/k$ is weakly etale
[def-weil-pbc-ind-etale-algebra], every finitely generated $k$-subalgebra of
$B$ is finite etale. In particular $B$ is ind-etale, is reduced, and all its
residue fields are separable algebraic over $k$.
