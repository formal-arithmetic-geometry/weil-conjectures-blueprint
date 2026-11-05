+++
kind  = "proof"
of    = "lem-fd-kernel-composition"
+++
Substituting the definitions and using
$p_2\circ r_{12}=r_2=q_1\circ r_{23}$, the base change of
[prop-functor-package] for the compact-support direct image along $q_1$
gives $q_1^*p_{2,!}\cong r_{23,!}r_{12}^*$, and the projection formula of
[prop-functor-package] for $r_{23}$ moves $r_{23}^*\mathcal K'$
inside; the composition law $q_2\circ r_{23}=r_3$ then gives

$$
\Phi_{\mathcal K'}\Phi_{\mathcal K}(K)
=r_{3,!}\bigl(r_1^*K\otimes^Lr_{12}^*\mathcal K\otimes^L
r_{23}^*\mathcal K'\bigr)[a+b],
\qquad r_1=p_1\circ r_{12}.
$$

The kernel transform with kernel $\mathcal K'\ast\mathcal K$ has the same
value: the projection formula for $r_{13}$ together with
$r_{13}^*s_1^*\cong r_1^*$, $s_2\circ r_{13}=r_3$ and the composition law
turns it into the same expression. Comparing the two expressions identifies
the kernels, and the shift is $[a]+[b]$ because the two shifts are those of
the two factors.
