+++
kind  = "proof"
of    = "lem-wf-weil-group-constant-extension"
+++
Use the finite-field datum of [def-weil-finite-field-fiber]. A finite
etale cover of $X_0^{(m)}$ is the same as a finite etale cover of $X_0$
whose constant-field action factors through
$\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_{q^m})$: this follows
directly by pulling a finite etale algebra along
$\mathbf F_q\subseteq\mathbf F_{q^m}$, and descending it along the finite
Galois action. Consequently the induced arithmetic fundamental group is
the inverse image of
$\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_{q^m})$ inside the
arithmetic fundamental group of $X_0$. The geometric kernel is unchanged,
because both geometric fibres equal $X$.

The geometric Frobenius over $\mathbf F_{q^m}$ is the $m$-th power of
the geometric Frobenius over $\mathbf F_q$, by the convention of
[def-tw-frobenius-action]. Taking the inverse image of the cyclic
group it generates in the exact sequence of [def-wf-weil-group],
whose degree-zero part is the geometric subgroup $\pi_1(X)$ by
[lem-wf-weil-group-exact-sequence], therefore gives exactly
$\deg^{-1}(m\mathbf Z)$. Dividing the old degree by $m$ sends this
Frobenius, and hence $s^m$, to one, which proves the normalized-degree
formula.
