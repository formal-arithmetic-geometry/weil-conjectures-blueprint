+++
id = "det-def-sfb-qlbar-condensed-subextensions"
kind = "lemma"
title = "Finite subextensions of $\\overline{\\mathbf Q}_\\ell$ form a directed poset"
lean = ["PadicAlgCl.FiniteIntermediateField", "IntermediateField.finiteDimensional_sup", "IntermediateField.finrank_sup_le", "IntermediateField.finiteDimensional_iSup_of_finite", "IntermediateField.finiteDimensional_adjoin"]
order = 1234
+++
Let $\ell$ be a prime and $\Qlb$ an algebraic closure of $\mathbf Q_\ell$. A *finite subextension*
is an intermediate field $\mathbf Q_\ell\subseteq E\subseteq\Qlb$ with $[E:\mathbf Q_\ell]<\infty$.
Then:

1. for finite subextensions $E_1,\dots,E_n$, the compositum $E_1\cdots E_n\subseteq\Qlb$ is a finite
   subextension containing each $E_\nu$, with $[E_1\cdots E_n:\mathbf Q_\ell]\le\prod_\nu[E_\nu:\mathbf Q_\ell]$;
   in particular the finite subextensions, ordered by inclusion, form a directed poset;
2. every finite subset of $\Qlb$ lies in a finite subextension, and $\Qlb$ is the union of the
   finite subextensions.
