+++
kind  = "proof"
of    = "lemma-nagata-glue-noetherian-stage"
uses = ["def-nagata-affine-gluing-valid-stage"]
+++
The gluing axioms hold at each valid stage, so the schemes are defined.
Each one is covered by finitely many spectra of finitely generated
$\mathbf Z$-algebras, proving finite type. On the chosen charts each
transition is affine by construction; the indexing refinement makes those
charts cover every inverse image, proving global affineness.

For the limit property, a cone over a cofiltered system of schemes is a
limit cone as soon as its restrictions over the members of an open cover
of one stage are limit cones. Use the stage $\lambda_0=\lambda_{\mathrm{glue}}(S)$
and its charts $\operatorname{Spec}(A_{\lambda_0,a})$. Over such a chart
the system restricts to the spectra $\operatorname{Spec}(A_{\lambda,a})$,
$\lambda\geq\lambda_0$, and the cone restricts to the maps
$U_a\to\operatorname{Spec}(A_{\lambda,a})$. The valid stages are directed
([lemma-nagata-valid-refinements-directed]) and cofinal
([def-nagata-affine-gluing-valid-stage]), so every section of
$\Gamma(S,U_a)$ lies in some $A_{\lambda,a}$ and $\Gamma(S,U_a)$ is the
directed union of the $A_{\lambda,a}$. Since $\operatorname{Spec}$ takes
filtered colimits of rings to limits, the restricted cone exhibits
$U_a=\operatorname{Spec}\Gamma(S,U_a)$ as
$\varprojlim_\lambda\operatorname{Spec}(A_{\lambda,a})$. Hence $\kappa_S$
is a limit cone, and together with the first part the glued stages form a
Noetherian approximation of $S$.
