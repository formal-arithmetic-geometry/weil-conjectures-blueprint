+++
kind  = "proof"
of    = "thm-pur-trace-normalization-transitivity"
+++
Step 1: the transitivity. Expanding the two composites with
[def-pur-smooth-trace], the left-hand composite is

$$
\begin{gathered}
Rg_!Rf_!Lf^*Lg^*K(d+e)[2d+2e]
\\
\xrightarrow{\ Rg_!Rf_!(\gamma_{f,Lg^*K(e)[2e]})\ }
Rg_!Rf_!Rf^!Lg^*K(e)[2e]
\\
\xrightarrow{\ Rg_!(\operatorname{Tr}_{f,Lg^*K(e)[2e]})\ }
Rg_!Lg^*K(e)[2e]
\\
\xrightarrow{\ \operatorname{Tr}^{\mathrm{sm}}_{g,K}\ }K,
\end{gathered}
$$

where the first arrow is the $\alpha_{g,f}^{-1}$-identification of the
statement (the pullback-composition and twist-additivity identifications,
all canonical), and the trace $\operatorname{Tr}_{f,Lg^*K(e)[2e]}$ is
the counit of $Rf_!\dashv Rf^!$ evaluated on $Lg^*K(e)[2e]$. The
transposed form of the purity–composition coherence
[thm-pur-composition-coherence] says that
$Rf_!(\gamma_{f,Lg^*K(e)[2e]})$ followed by the counit is the counit
of $Rf_!\dashv Rf^!$ applied to the object $Lf^*Lg^*K(d+e)[2d+2e]$
through the composition isomorphism $c_{g,f}$ – it identifies
$Rf_!Rf^!Lg^*K(e)[2e]$ with $Rf_!Lf^*Lg^*K(d+e)[2d+2e]$ – so the
composite of the last three displayed arrows is exactly the
$f$-trace $Rg_!(\operatorname{Tr}^{\mathrm{sm}}_{f,Lg^*K(e)[2e]})$,
which is what the statement's composite applies. The remaining
identification is the functoriality of the counits with respect to the
canonical identification $R(gf)_!\cong Rg_!Rf_!$ (the $\alpha_{g,f}$
of [thm-sf-comp-composition]), the compatibility of the
adjunction with composition being the transpose of the composition
isomorphism of the $R^!$-side (the composition
isomorphism of the $R_!$-side is the transpose of the one of the
$R^!$-side, and the triangle identity of the adjunction
$Rf_!\dashv Rf^!$ is used once, in the form
$\operatorname{Tr}_f\circ Rf_!(\gamma_{f,K})=\operatorname{Tr}_{f,K}$).
Hence the two composites agree, which is the transitivity.
Step 2: the normalization on the geometric fiber. For
$f=p_d:\mathbf A^d\to\Spec k$, the smooth trace
$\operatorname{Tr}^{\mathrm{sm}}_{p_d,\Lambda}$ is, by
[def-pur-smooth-trace], $R\Gamma_c(\gamma_{p_d,\Lambda})$ followed
by the counit, and by the agreement
[lem-pur-projection-purity-agreement] the purity map
$\gamma_{p_d,\Lambda}$ is the affinity-space purity comparison, i.e. the affinity-space integration of
[cor-pur-affine-space-purity]; by induction on $d$ with Step 1
(the case $d+e$ with $e=1$: the $d$-fold trace is the iterate of
the one-fold trace), and with the case $d=1$ being
[thm-pur-affine-line-purity] in adjoint form (the
affine-line integration $\int_p$, the adjoint of the projective-line
trace normalized by $t_q(c_1(\mathcal O(1)))=1$, sends the Cartier class
of the zero section to $1$ and the class of the orientation
$\operatorname{pur}_s=\partial\kappa(t)$ of
[thm-pur-affine-line-orientation], which is minus the Cartier class, to
$-1$, by [cor-pur-affine-space-zero-section-purity] with $c=1$), the
trace of the ordered fundamental class, the $d$-fold tensor of the
affine-line classes, is the product of the images, i.e.

$$
\operatorname{Tr}^{\mathrm{sm}}_{p_d,\Lambda}\bigl(\underbrace{\partial\kappa(t_1)\otimes\cdots\otimes\partial\kappa(t_d)}\bigr)=(-1)^d\in\Lambda,
$$

and likewise the $d$-fold tensor of the Cartier classes goes to $1$;
this agrees with [cor-pur-affine-space-zero-section-purity] for
$B=\Spec k$, $c=d$. The intermediate Koszul signs in the
reassociations are $+1$ by [cor-pur-affine-space-purity] (the shift
factors are of even degree). Step 3: the base-change compatibility. The smooth trace is
compatible with the base change of $Z$ by the conjugation of
[thm-pur-smooth-base-change-coherence] with the compact-support
base change of the adjunctions (the trace is the counit, the counit of
the pulled-back adjunction is the pullback of the counit under the
base-change maps: the base-change compatibility of the adjunction
$Rf_!\dashv Rf^!$). Step 4: the coefficient
compatibilities. The compatibility with finite reduction is
[thm-pur-finite-reduction-of-purity]: the trace is built from
the purity isomorphism and the counit, and both reduce compatibly.
For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$ the transitivity and base change
are [sk-prop-sp-trace-composition] and [sk-prop-sp-purity-bc]. The
normalization on $\mathbf A^d$ holds because these traces are, by
[det-sp-purity-coefficient-change], the derived limit, the
rationalization and the scalar extension of the finite traces, and these
operations send $\pm1$ to $\pm1$.
