+++
kind = "proof"
of = "lemma-extension-across-finite-subset"
order = 571
+++
Lemma [lemma-smooth-morphisms-locally-constant-sheaves] controls the
direct image $R(bj)_*F$ of $Rj_*F$ to $S$.
Lemma [lemma-detection-proper-direct-image] turns this, together with
the hypothesis on $G$, into control of $Rj_*F$ along $Z$. We work on the
étale sites.

For constructibility we check the hypotheses of part (1) of
Lemma [lemma-detection-proper-direct-image] for $K=Rj_*F$ and
$U=G$. The complex $Rj_*F$ lies in $D^+(Y_{\acute{e}t},\Fell)$ because $F$ is a
sheaf. Its restriction to $G$ is in $\Dbc$ by assumption, and
$Z=Y\setminus G$ is finite over $S$. It remains to treat the direct image.
Since $bj:X\to S$ is smooth and $F$ is locally constant, we may apply
Lemma [lemma-smooth-morphisms-locally-constant-sheaves]. After
shrinking $S$ to a nonempty open $S_0$, the complex $Rb_*Rj_*F=R(bj)_*F$
lies in $\Dbc(S_0,\Fell)$, and its formation commutes with base change
along every $T\to S_0$ of finite type over $k$. Part (1) of
Lemma [lemma-detection-proper-direct-image] then gives
$Rj_*F\in\Dbc(Y_{S_0},\Fell)$.

For base change we use part (2) of the lemma instead. Let $T\to S_0$ be a
$k$-scheme of finite type, and let $\varphi$ be the base change map
$g_Y^*Rj_*F\to Rj_{T,*}g_X^*F$. By assumption it is an isomorphism on
$G_T$. Proper base change for $b$ and the compatibility of base change maps
with composition [Stacks, [0E46](https://stacks.math.columbia.edu/tag/0E46)] identify $Rb_{T,*}\varphi$ with the base
change map for $R(bj)_*F$, which is an isomorphism. Since $b_T$ is proper
and $b_Ti_T$ is finite, part (2) of
Lemma [lemma-detection-proper-direct-image] applies over $T$. It shows
that $\varphi$ is an isomorphism.
