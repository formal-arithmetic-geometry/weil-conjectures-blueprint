+++
id = "def-pc-separably-closed"
kind = "definition"
title = "Separably closed fields"
lean = ["IsSepClosed", "IsSepClosed.iff_exists_root", "IsSepClosed.iff_forall_finrank_eq_one", "IsSepClosure"]
order = 754
+++
A field $k$ is *separably closed* if every nonconstant separable
polynomial $f\in k[T]$ has a root in $k$ (equivalently, $k$ has no
nontrivial finite separable field extension; the equivalence of the two
formulations is [lem-pc-sepclosed-finite-sep-trivial]). A *separable closure* of a field $k$ is a separable algebraic extension
of $k$ which is separably closed.
