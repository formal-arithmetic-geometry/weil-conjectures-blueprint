+++
kind = "proof"
of = "det-pe-morphisms-etale-comparison"
+++
*4.* Flatness is local on source and target. The diagonal $\Delta_u$ maps the affine open
$\operatorname{Spec}B$ into the affine open
$\operatorname{Spec}B\times_{\operatorname{Spec}R}\operatorname{Spec}B=\operatorname{Spec}(B\otimes_RB)$,
where it is the closed immersion given by multiplication $B\otimes_RB\to B$; such opens
cover the source of $\Delta_u$ and their images lie in opens of this form covering a
neighbourhood of $\Delta_u(U)$. Hence $u$ and $\Delta_u$ are flat if and only if all the
chart maps $R\to B$ and $B\otimes_RB\to B$ are flat.

*1.* An étale morphism is flat. It is also unramified and locally of finite presentation,
so its diagonal is an open immersion (Stacks Project, Morphisms, unramified morphisms), and open immersions are flat.

*2.* An ind-étale ring map is weakly étale by [lem-weil-pbc-ind-etale-stability]: $B$ is
flat over $R$ as a filtered colimit of flat algebras, and $B\otimes_RB\to B$ is
ind-Zariski, hence flat. Apply 4.

*3.* Let $u$ be weakly étale and locally of finite presentation. The diagonal of a
morphism locally of finite presentation is locally of finite presentation (Stacks Project, Morphisms, morphisms locally of finite presentation). The diagonal is a monomorphism, and it is flat by assumption. A flat monomorphism
locally of finite presentation is an open immersion (Stacks Project, Étale morphisms of schemes). So $\Delta_u$ is
an open immersion, i.e. $u$ is unramified (Stacks Project, Morphisms, unramified morphisms). A flat, unramified morphism
locally of finite presentation is étale.
