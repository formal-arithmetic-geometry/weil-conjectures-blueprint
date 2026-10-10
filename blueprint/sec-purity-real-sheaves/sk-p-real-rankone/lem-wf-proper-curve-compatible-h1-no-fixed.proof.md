+++
kind  = "proof"
of    = "lem-wf-proper-curve-compatible-h1-no-fixed"
+++
Let $J$ be the Jacobian of $C$, with the semilinear action of arithmetic
Frobenius $\sigma_Q$ supplied by
[lem-wf-geometric-jacobian-galois-action], so that the geometric action
on the Kummer-identified
twisted cohomology is $\sigma_Q^{-1}$. By
[lem-wf-curve-h1-dual-tate-module], the module in (4.4) is

$$
T_\ell J^\vee:=\operatorname{Hom}_{\mathbf Z_\ell}
(T_\ell J,\mathbf Z_\ell),
$$

with the action determined by the perfect pairing and its twisted
equivariance in [thm-pod-equivariance-of-the-twisted-pairing]. In a
chosen $\mathbf Z_\ell$-basis of $T_\ell J$, write the matrix of
$\sigma_Q$ as $B$. The geometric action on the second factor of the
pairing is $B^{-1}$. Equivariance of the pairing says that the geometric
action on the first factor is

$$
(B^{-1})^{-t}=B^t.
$$

By [lem-wf-finite-field-tate-no-fixed], $B-1$ is injective on
the finite free module $T_\ell J$. Over the domain $\mathbf Z_\ell$,
this says $\det(B-1)\ne0$: after tensoring with $\mathbf Q_\ell$, an
injective endomorphism of a finite-dimensional vector space is invertible.
Since
$\det(B^t-1)=\det(B-1)\ne0$, the transpose $B^t-1$ is likewise
injective on the finite free dual $T_\ell J^\vee$. This is exactly the
assertion that (4.4) has no $\Phi_Q$-fixed element.
