+++
kind  = "proof"
of    = "def-nagata-morphism-descent"
+++
We show that such a stage and morphism exist. Choose a finite affine cover
of $Y_{\lambda_0}$, descend the quasi-compact inverse images under
$\varphi$ of its base changes to quasi-compact opens of some $X_\lambda$
([def-nagata-qc-open-descent]), choose finite affine covers of those opens,
and descend each affine ring map using its finite generator-and-relation
data and [lemma-nagata-filtered-colimit-finite-data]. Retain the
comparison isomorphisms for each descended open, transport every affine map
through them, and include the finitely many stages at which the local maps
agree on pairwise overlaps in one common upper bound; the transported maps
glue there to an $S_\lambda$-morphism whose base change to $S$ is
$\varphi$.
