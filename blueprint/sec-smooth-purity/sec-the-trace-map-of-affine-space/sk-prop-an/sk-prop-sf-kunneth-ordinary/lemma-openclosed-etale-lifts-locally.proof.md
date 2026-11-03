+++
kind  = "proof"
of    = "lemma-openclosed-etale-lifts-locally"
uses = ["lemma-openclosed-standard-etale-lift"]
+++
The assertion is local at $w$, so we may shrink $X$, $Z$ and $W$ around
$i(q(w))$ and $w$. Choose an affine open $\Spec R\subseteq X$ containing
$i(q(w))$; then $Z$ meets it in $\Spec R/I$, and we may choose an affine open
$\Spec B\subseteq W$ containing $w$ and lying over $\Spec R/I$, so that $B$
is an étale $R/I$-algebra.

By the local structure of étale algebras, after replacing $\Spec B$ by a
basic open subscheme containing $w$ we may assume that $B$ is a standard
étale $R/I$-algebra. By
[lemma-openclosed-standard-etale-lift] there is a standard étale
$R$-algebra $A$ with $(R/I)\otimes_RA\cong B$. Put
$V:=\Spec A$, mapping to $X$ through $\Spec A\to\Spec R\subseteq X$; this is
étale, being an étale morphism followed by an open immersion. Finally

$$
V\times_XZ=\Spec A\times_{\Spec R}\Spec R/I=\Spec\bigl((R/I)\otimes_RA\bigr)
\cong\Spec B=:W_0,
$$

which is an open subscheme of $W$ containing $w$.
