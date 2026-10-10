+++
kind  = "proof"
of    = "lem-wf-determinantal-weight-exists"
+++
The determinant line $\det(\mathcal V)=\bigwedge^r\mathcal V$ of
[def-mg-determinant-line] is a lisse Weil sheaf of rank one on
$X_0$. With respect to the fundamental representation of
[def-wf-fundamental-representation] it is given by the continuous
character $\chi_{\det}=\det\circ\rho_{\mathcal V}$ of $W(X_0,\bar x)$
with values in the finite coefficient field $E$ over which
$\mathcal V$ is defined. The finite geometric image theorem
[thm-wf-rank-one-finite-geometric-image-curve], applied to the normal
geometrically connected curve $X_0$ and to $\chi_{\det}$, says that
$\chi_{\det}(\pi_1(X))$ is finite; hence the purity statement of
[cor-wf-rank-one-punctual-purity-curve] applies to
$\det(\mathcal V)$ and exhibits a real number $a$ with
$|\iota(\alpha)|=q_y^{a/2}$ for every closed point $y\in|X_0|$ and
every eigenvalue $\alpha$ of the local geometric-Frobenius operator
$F_y$ of [def-weil-local-frobenius-trace]. This is punctual
$\iota$-purity of weight $a$ in the sense of
[def-weil-punctual-weights].

For uniqueness, suppose that $\det(\mathcal V)$ is punctually
$\iota$-pure of weights $a$ and $a'$ in the sense of
[def-weil-punctual-weights]. The curve $X_0$ has a closed point
$y$. The operator $F_y$ of
[def-weil-local-frobenius-trace] is an automorphism of the
one-dimensional stalk at $y$, because the Weil structure of
$\det(\mathcal V)$ is an isomorphism, so $F_y$ has a nonzero
eigenvalue $\alpha$; then
$q_y^{a/2}=|\iota(\alpha)|=q_y^{a'/2}$ with
$q_y=\#\kappa(y)>1$, so $a=a'$.
