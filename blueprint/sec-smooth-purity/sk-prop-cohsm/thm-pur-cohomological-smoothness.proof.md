+++
kind  = "proof"
of    = "thm-pur-cohomological-smoothness"
+++
Work at a finite coefficient stage. The earlier orientation-free
theorem [thm-asd-smooth-tensor] proves the canonical tensor
formula on the ordinary etale site and shows that
$\omega_f[-2d]$ is a locally constant free rank-one sheaf.
In particular it is tensor-invertible, and tensoring it with the
pullback of a bounded constructible finite-Tor complex stays in that
category. The actual-adjoint comparison
[thm-sf-ambient-adjoint-class] and
[thm-weil-pbc-site-comparison] transport the tensor map and
its isomorphy to the finite etale-origin objects used here.
Because the map is obtained by transposing the projection formula
and counit on both sites, the transported map is the canonical
$\theta_{f,K}$ in [def-pur-co-smoothness].

For the third condition of that definition,
[lem-pur-smb-extraordinary] proves arbitrary base change of the
actual right adjoint, and [prop-asd-smooth-base-change] also
proves its compatibility with the tensor transformation before
transport. Thus these are all three conditions of cohomological
smoothness. For composition, [lem-pur-co-smooth-composition]
identifies $\omega_{gf}$ with
$\omega_f\otimes^LLf^*\omega_g$. The two tensor transformations
agree: transposing them gives the projection formula followed by
the same two counits, composed in their adjunction order. This
proves the fourth assertion without using an orientation of $f$.
