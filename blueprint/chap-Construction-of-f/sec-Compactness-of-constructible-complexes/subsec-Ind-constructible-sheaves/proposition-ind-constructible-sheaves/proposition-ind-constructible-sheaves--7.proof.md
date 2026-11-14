+++
kind = "proof"
of = "proposition-ind-constructible-sheaves--7"
order = 453015
uses = ["definition-lisse-sheaves", "lemma-continuity-ext-out-constructible-complex", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--3", "definition-constructible-sheaves--4", "lemma-constructible-sheaves--3", "lemma-continuity-ext-out-constructible-complex--1", "proposition-ind-constructible-sheaves--2"]
+++
*Extensions.* Let $0\to N\to M\to B\to0$ be exact in
$\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$, with $N=\varinjlim_\beta D_\beta$ and
$B=\varinjlim_\alpha C_\alpha$ ind-constructible. We show that $M$ is a
filtered colimit of extensions of constructible sheaves. First, the pullback
of the extension along $C_\alpha\to B$ is ind-constructible. Its class lies in
$\Ext^1(C_\alpha,N)$, and
Lemma [lemma-continuity-ext-out-constructible-complex] gives

$$
\Ext^1(C_\alpha,N)
=\varinjlim_\beta\Ext^1(C_\alpha,D_\beta).
$$

So the pulled-back extension is pushed out from an extension $M_{\alpha\beta}$
of $C_\alpha$ by some $D_\beta$. Since
$\Cons(X,\Lambda)$ is closed under extensions, $M_{\alpha\beta}$ and each of its
pushouts along $D_\beta\to D_{\beta'}$ are constructible. Their colimit over
$\beta'$ is the pullback of $M$ to $C_\alpha$. Second, since filtered
colimits are exact, $M$ is the colimit over $\alpha$ of these pullbacks.
By closure under filtered colimits, $M\in\IndCons(X,\Lambda)$.

*Source:* the proof of Proposition [proposition-ind-constructible-sheaves].
