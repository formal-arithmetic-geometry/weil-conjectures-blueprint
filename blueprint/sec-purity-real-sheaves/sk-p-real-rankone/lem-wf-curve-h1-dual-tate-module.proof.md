+++
kind  = "proof"
of    = "lem-wf-curve-h1-dual-tate-module"
+++
At level $n$, the finite-level pairing lemma
[lem-wf-curve-finite-level-pd] gives the adjoint isomorphism

$$
H^1(C,A_n)\xrightarrow{\sim}
\operatorname{Hom}_{A_n}\bigl(H^1(C,A_n(1)),A_n\bigr).
\tag{4.2}
$$

The equivariance and compatibility under reduction are those of
[thm-pod-equivariance-of-the-twisted-pairing]. By
[lem-wf-curve-kummer-jacobian-tate-module], the second factor is
$J[\ell^n](\overline{k}_0)$. Thus (4.2) gives natural compatible
Galois-equivariant isomorphisms

$$
H^1(C,A_n)\xrightarrow{\sim}
\operatorname{Hom}_{A_n}
\bigl(J[\ell^n](\overline{k}_0),A_n\bigr).
\tag{4.3}
$$

The transition maps
$J[\ell^{n+1}](\overline{k}_0)\xrightarrow{[\ell]} J[\ell^n](\overline{k}_0)$ are surjective by
[thm-av-final](d). We spell out the resulting quotient
description. Put $r=2\dim J$. By
[thm-av-final](c), the level-one group is
$(\mathbf Z/\ell\mathbf Z)^r$; choose a basis and lift its vectors
successively through the displayed surjections. At level $n$, the chosen
lifts form a basis of the free
$\mathbf Z/\ell^n\mathbf Z$-module $J[\ell^n](\overline{k}_0)$: their
reductions form a basis modulo $\ell$, so elementary Nakayama (or the
usual row-reduction over the local ring $\mathbf Z/\ell^n\mathbf Z$)
shows that they generate, and equality of the cardinalities
$\ell^{nr}$ makes the resulting surjection an isomorphism. The compatible
bases identify the whole inverse system with
$(\mathbf Z/\ell^n\mathbf Z)^r$ under reduction. Consequently
$T_\ell J\cong\mathbf Z_\ell^r$ ([thm-av-final](d)), every projection is surjective, and its
kernel is exactly $\ell^nT_\ell J$. Thus the projections give canonical
isomorphisms (independent of the bases used to prove them)

$$
J[\ell^n](\overline{k}_0)\cong T_\ell J/\ell^nT_\ell J.
$$

Consequently

$$
\varprojlim_n\operatorname{Hom}_{A_n}
(J[\ell^n](\overline{k}_0),A_n)
\cong
\varprojlim_n\operatorname{Hom}_{\mathbf Z_\ell}
(T_\ell J/\ell^nT_\ell J,\mathbf Z_\ell/\ell^n\mathbf Z)
\cong \operatorname{Hom}_{\mathbf Z_\ell}(T_\ell J,\mathbf Z_\ell).
$$

The last map sends a homomorphism to its reductions; it is bijective because
$T_\ell J$ is finite free over $\mathbf Z_\ell$, as just proved. Only
ordinary inverse limits are used here; no derived-limit comparison is being
invoked. Although bases were used to verify the quotient description, the
projections, pairings, and reduction maps themselves are canonical and
Galois equivariant. This proves (4.1) with its Galois action.
