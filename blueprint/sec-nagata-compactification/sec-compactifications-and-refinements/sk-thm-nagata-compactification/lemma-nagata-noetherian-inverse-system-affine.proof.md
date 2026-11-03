+++
kind  = "proof"
of    = "lemma-nagata-noetherian-inverse-system-affine"
uses = ["lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-nagata-ring-finite-type-subalgebras"]
+++
Finitely generated $\mathbf Z$-subalgebras are directed by
[lemma-nagata-ring-finite-type-subalgebras], and each
$\operatorname{Spec}(A_0)$ is of finite type over $\mathbf Z$, hence
Noetherian by the Hilbert basis theorem. Every transition morphism is
$\operatorname{Spec}$ of a ring map and therefore affine. By the same
lemma, $A$ is the filtered colimit of the $A_0$; since $\operatorname{Spec}$
is a right adjoint it takes this colimit of rings to a limit of schemes, so
$S=\varprojlim\operatorname{Spec}(A_0)$.
