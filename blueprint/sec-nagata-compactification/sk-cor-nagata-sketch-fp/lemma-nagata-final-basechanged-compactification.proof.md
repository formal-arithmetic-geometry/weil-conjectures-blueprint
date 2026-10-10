+++
kind  = "proof"
of    = "lemma-nagata-final-basechanged-compactification"
+++
A separated morphism is quasi-separated, so $Y\to S$ is quasi-compact,
quasi-separated and locally of finite presentation, i.e. of finite
presentation, and the descended model of
[lemma-nagata-final-descended-model] is defined: a separated morphism
$Y_{\lambda_Y}\to S_{\lambda_Y}$ of finite presentation over a Noetherian
base $S_{\lambda_Y}$, together with an isomorphism
$\epsilon_Y\colon Y_{\lambda_Y}\times_{S_{\lambda_Y}}S\to Y$ over $S$.

By [lemma-nagata-final-noetherian-compactification], $C_{Y,\lambda_Y}$ is a
compactification $Y_{\lambda_Y}\hookrightarrow\overline Y_{\lambda_Y}\to
S_{\lambda_Y}$. By [lemma-nagata-compactification-base-change] its base
change along $S\to S_{\lambda_Y}$ is a compactification of
$Y_{\lambda_Y}\times_{S_{\lambda_Y}}S\to S$: an open immersion
$Y_{\lambda_Y}\times_{S_{\lambda_Y}}S\hookrightarrow\overline Y$ followed by
a proper morphism $\overline Y\to S$. Precomposing the open immersion with
the isomorphism $\epsilon_Y^{-1}$ gives the factorization
$\mathsf C^{\mathrm{fp}}(Y/S)$ of
[def-nagata-final-basechanged-compactification]. Its first map is again an
open immersion, its second map is proper, and since $\epsilon_Y$ is a
morphism over $S$ the composite is $Y\to S$. Thus
$\mathsf C^{\mathrm{fp}}(Y/S)$ is a compactification of $Y\to S$, and
$Y\to S$ is compactifiable in the sense of [def-nagata-compactifiable].
