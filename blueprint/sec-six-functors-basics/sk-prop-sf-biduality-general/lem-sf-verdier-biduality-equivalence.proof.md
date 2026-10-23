+++
kind  = "proof"
of    = "lem-sf-verdier-biduality-equivalence"
+++
(1) is the finite-stage étale biduality theorem
[thm-weil-etale-geometric-biduality] for the algebraically closed field $k$
and the finite coefficient ring $\Lambda$, whose exponent is invertible on
$k$. The isomorphism $K\cong\mathbb D_X\mathbb D_XK$ is $\delta_K$ itself.

(2) An algebraically closed field is perfect, so $\mathbb D_X$ carries
$D^b_{ctf}(X,\Lambda)$ into itself by
[lem-weil-verdier-preservation-strata]. Regard $\mathbb D_X$ as a functor
$D(X_{\Et},\Lambda)^{\mathrm{op}}\to D(X_{\Et},\Lambda)$. Transposing the
evaluation pairing of [lem-weil-duality-pairing] and using the symmetry of
$\otimes^L_\Lambda$ gives bijections
$$
\operatorname{Hom}(L,\mathbb D_XK)\cong
\operatorname{Hom}(L\otimes^L_\Lambda K,\omega_X)\cong
\operatorname{Hom}(K,\mathbb D_XL),
$$
natural in $K$ and $L$. Thus $\mathbb D_X^{\mathrm{op}}$ is left adjoint to
$\mathbb D_X$, and both the unit and, read in the opposite category, the counit
of this adjunction are the double-dual morphisms $\delta$. Restrict the
adjunction to $D^b_{ctf}(X,\Lambda)$, which both functors preserve. There the
unit and the counit are isomorphisms by (1), so the restricted adjunction is an
adjoint equivalence with quasi-inverse $\mathbb D_X$.
