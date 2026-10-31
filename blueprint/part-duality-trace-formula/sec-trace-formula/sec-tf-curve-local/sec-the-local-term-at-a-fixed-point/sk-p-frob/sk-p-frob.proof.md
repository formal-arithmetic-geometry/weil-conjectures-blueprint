+++
kind = "proof"
of = "sk-p-frob"
uses = ["sk-i-additivity", "sk-i-curve-zero", "sk-p-proper", "sk-p-pairing", "sk-lem-tf-fixed-points", "sk-d-weil", "sk-lem-tf-curve-restriction-zero"]
+++
We cut $K$ into its parts on $X\setminus\{y\}$ and on $y$.
The first has zero stalk at $y$, so its local term vanishes, and the
second lives on a point.
Let $i:\{y\}\hookrightarrow X$ and $j:U=X\setminus\{y\}\hookrightarrow X$.
Both pieces are stable under $\Phi_X^m$, and in fact
$((\Phi_X^m)^{-1}\{y\})_{\mathrm{red}}=\{y\}$. In the enhanced derived
category, the functorial localization triangle is a two-step filtered
object,

$$
K_U=j_!j^*K\longrightarrow K\longrightarrow i_*i^*K
\xrightarrow{+1}.
$$

Using two base change identities, we see that $\psi$ induces a coherent
map from the $(\Phi_X^m)^*$-pullback of this filtration to the filtration itself.
For the open part, base change along inverse
images in the cartesian square shows that
$(\Phi_X^m)^*j_!\simeq j_!(\Phi_X^m|_U)^*$. The square for the point is cartesian only
after passing to reductions, so we use proper base change followed by
nilpotent invariance to see that $(\Phi_X^m)^*i_*\simeq i_*(\Phi_X^m|_y)^*$. Both comparisons are mates of the
adjunction units for $j$ and $i$ used in the triangle, and the two
induced correspondences are $\psi_U$ and $i_*\psi_{\bar y}$.

By additivity of trace classes
(Proposition [sk-i-additivity]) we have

$$
\operatorname{LT}_y(\psi)
=\operatorname{LT}_y(\psi_U)
+\operatorname{LT}_y(i_*\psi_{\bar y}).
$$

The first term is zero by
Lemma [sk-lem-tf-curve-restriction-zero], since
$(K_U)_{\bar y}=0$. By the description of the induced correspondence $u_Z$ in
Proposition [sk-i-additivity], the correspondence
$i_*\psi_{\bar y}$ is the pushforward along $i$ of the cohomological
correspondence $\psi_{\bar y}$ on $(y,K_{\bar y})$ for the identity
correspondence of $y$. By the
compatibility with proper pushforward in
Theorem [sk-p-proper] and by
Lemma [sk-p-pairing], its local term equals
$\operatorname{tr}_A(\psi_{\bar y}\mid K_{\bar y})$, the trace on
the perfect complex $K_{\bar y}$.
