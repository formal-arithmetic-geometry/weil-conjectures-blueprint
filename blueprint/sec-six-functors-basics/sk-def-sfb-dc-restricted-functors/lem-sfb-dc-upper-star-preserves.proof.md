+++
kind  = "proof"
of    = "lem-sfb-dc-upper-star-preserves"
uses = ["sk-def-sfb-constructible", "sk-def-sfb-module-pushforward-pullback", "sk-prop-sfb-module-derived-factorization", "sk-prop-sfb-module-pullback-exact"]
+++
The module-object pullback $f^*$ is exact ([sk-prop-sfb-module-pullback-exact]), and
$Lf^*\cong D(f^*)$ is computed levelwise ([sk-prop-sfb-module-derived-factorization]). Hence
$H^q(Lf^*K)\cong f^*H^q(K)$ for all $q$, so $Lf^*K$ is bounded. It remains to show that $f^*M$
is constructible ([sk-def-sfb-constructible]) for a constructible $\Lambda_Y$-module $M$. Let
$Y=\bigsqcup_aY_a$ be a finite stratification such that each $M|_{Y_a}$ is locally finitely
presented. Then the preimages $X_a=f^{-1}(Y_a)$ form a finite stratification of $X$ by locally
closed subschemes. Since pullbacks compose ([sk-def-sfb-module-pushforward-pullback]),
$(f^*M)|_{X_a}$ is the pullback of $M|_{Y_a}$ along $f_a\colon X_a\to Y_a$. Choose a pro-étale cover
$\{U_i\to Y_a\}$ with $M|_{U_i}\cong\operatorname{coker}(\Lambda^m\to\Lambda^n)$. Its base change
$\{U_i\times_{Y_a}X_a\to X_a\}$ is a pro-étale cover. The pullback is right exact, and it carries
free modules of finite rank to free modules of the same rank. So on this cover the restrictions
of $f^*M$ are again cokernels of maps between finite free modules.
