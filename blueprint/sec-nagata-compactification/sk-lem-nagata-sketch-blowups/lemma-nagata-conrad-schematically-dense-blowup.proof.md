+++
kind  = "proof"
of    = "lemma-nagata-conrad-schematically-dense-blowup"
uses = ["def-nagata-qc-open-complement-ideal", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-admissible-blowup-preserves-density", "thm-nagata-global-blowup-proper", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-qc-open-complement-ideal-exists"]
+++
*First assertion.* By [lemma-nagata-qc-open-complement-ideal-exists]
there is a finite type quasi-coherent ideal
$\mathcal I_0\subseteq\mathcal O_X$ with $V(\mathcal I_0)=X\setminus U$.
Its blow-up $X_1\to X$ is $U$-admissible, and the inverse image of
$U=X\setminus V(\mathcal I_0)$ is scheme-theoretically dense in $X_1$ by
the last assertion of [lemma-nagata-conrad-dense-in-admissible-blowup].

*Second assertion.* Let $\pi\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$
be $U$-admissible. Since $\mathcal I$ is of finite type, $\pi$ is proper
([thm-nagata-global-blowup-proper]); hence $\widetilde X$ is again
quasi-compact and quasi-separated, and $\widetilde U=\pi^{-1}(U)$ is a
quasi-compact open of $\widetilde X$. Apply the first assertion to
$\widetilde U\subseteq\widetilde X$: there is a finite type ideal
$\mathcal I_2$ on $\widetilde X$ with
$V(\mathcal I_2)=\widetilde X\setminus\widetilde U$ whose blow-up
$q\colon X_2=\operatorname{Bl}_{\mathcal I_2}(\widetilde X)\to\widetilde X$ is
$\widetilde U$-admissible and in which $q^{-1}(\widetilde U)$ is
scheme-theoretically dense. By [lemma-nagata-admissible-blowup-comp]
there are a finite type ideal $\mathcal K$ on $X$ with
$V(\mathcal K)\cap U=\varnothing$ and an isomorphism
$\theta\colon X_1:=\operatorname{Bl}_{\mathcal K}(X)\xrightarrow{\sim}X_2$
over $X$. Then $X_1\to X$ is $U$-admissible, $q\circ\theta\colon X_1\to\widetilde X$
is a morphism over $X$, and the inverse image of $U$ in $X_1$ is
$\theta^{-1}(q^{-1}(\widetilde U))$, which is scheme-theoretically dense
because $\theta$ is an isomorphism.
