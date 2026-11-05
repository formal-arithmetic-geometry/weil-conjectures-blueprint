+++
kind  = "proof"
of    = "lemma-nagata-relative-stage-morphism-data-exists"
+++
Fix any index $\lambda_S$. The stage $S_{\lambda_S}$ is of finite type over
$\mathbf Z$, hence of finite presentation over $\mathbf Z$, so the morphism
$X\to S\to S_{\lambda_S}$ factors through some stage $X_{\lambda}$ of
$X=\varprojlim X_\lambda$ (Stacks Tag 01ZC): there is a morphism
$X_\lambda\to S_{\lambda_S}$ whose composite with $X\to X_\lambda$ is
$X\to S_{\lambda_S}$. For every larger index $\lambda_X\geq\lambda$ the
composite $X_{\lambda_X}\to X_\lambda\to S_{\lambda_S}$ still satisfies the
compatibility. Finally, since $X\to S$ is locally of finite type and $X$ is
quasi-compact, the induced comparison
$X\to X_{\lambda_X}\times_{S_{\lambda_S}}S$ is an immersion for
$\lambda_X$ large enough (the argument of Stacks Tag 01ZE: the finitely many
generators of the coordinate rings of a finite affine cover of $X$ over
affine opens of $S$ are defined at a finite stage).
