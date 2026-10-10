+++
kind  = "proof"
of    = "prop-ag-det-weight-exterior"
+++
Write $V$ for the Weil representation. The factors and their weights
are those of
[def-mg-weil-composition-series] and [d-weights]. The Weil
semisimplification $V^{\mathrm{ss}}=\bigoplus_aA_a$ of
[def-mg-weil-semisimplification] is a semisimple Weil representation,
so [lem-mg-common-positive-central-element] applies to it, giving
a central element $z$ of degree $d>0$ (in the monodromy data of
[def-wf-monodromy-data]). For each simple
factor $A_a$, its image is
central by [lem-mg-degree-component-functoriality]. Its matrix
commutes with the Weil-group image on $A_a$, so
[lem-wf-schur-scalar] applies to this Weil-simple representation and
gives a scalar $c_a$. The central-element formula
[cor-mg-central-determinant-weight], applicable because $A_a$ has
finite geometric determinant, gives

$$
\gamma_a=\frac{\lambda(c_a)}{d}.
$$

By [lem-mg-filtered-exterior-power], $\bigwedge^rV$ has a finite
Weil-stable filtration with nonzero successive quotients

$$
Q_{\boldsymbol n}=\bigotimes_{a=1}^t\bigwedge^{n_a}A_a,
\qquad 0\le n_a\le d_a,
\qquad \sum_a n_a=r,
$$

each a tensor construction on subquotients of $V^{\mathrm{ss}}$.
The refinement lemma [lem-mg-filtration-refinement] reduces all
composition factors to these quotients. On $Q_{\boldsymbol n}$, the
central element acts by $c_{\boldsymbol n}:=\prod_a c_a^{n_a}$. Every
simple factor $C$ of this quotient receives a central degree-$d$ element
by [lem-mg-degree-component-functoriality]; its matrix commutes with
the Weil-group image on $C$, and therefore is scalar by Schur's lemma.
Since $C$ has finite geometric determinant by assumption,
[cor-mg-central-determinant-weight] gives

$$
\dw_\lambda(C)=\frac{\lambda(c_{\boldsymbol n})}{d}
=\sum_a n_a\gamma_a.
$$

Grouping equal $\gamma_a$'s gives the asserted aggregate tuple and its
capacity bounds. Conversely, for an admissible tuple $(n_\gamma)$,
distribute each $n_\gamma$ among the indices with $\gamma_a=\gamma$,
never exceeding $d_a$. The resulting $Q_{\boldsymbol n}$ is nonzero,
so [lem-mg-composition-series-exists] gives a simple factor, whose
weight is the required sum. This proves the converse.
