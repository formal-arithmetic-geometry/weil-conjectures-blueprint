+++
kind  = "proof"
of    = "det-nagata-refinement-common-dense"
uses = ["lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-restrict-open", "lemma-nagata-open-immersion-qc-over-separated-target", "det-nagata-definition-refinement"]
+++
*Step 1: $\delta$ is a quasi-compact immersion.* Let
$P^\circ=\mathrm{pr}_1^{-1}(j_1(X))=X\times_S\overline X_2$, an open of $P$.
The map $\delta$ lands in $P^\circ$, and as a map to
$X\times_S\overline X_2$ it is the graph $\Gamma=(\mathrm{id}_X,j_2)$ of
$j_2:X\to\overline X_2$. Since $\overline X_2\to S$ is proper, hence
separated, the graph $\Gamma$ is a closed immersion (it is the base change
of the diagonal of $\overline X_2/S$ along $j_2\times\mathrm{id}$). The
open immersion $P^\circ\hookrightarrow P$ is the base change of $j_1$, which
is quasi-compact ([lemma-nagata-open-immersion-qc-over-separated-target]:
$p_1\circ j_1=f$ is quasi-compact and $p_1$ is separated). Hence
$\delta=(P^\circ\hookrightarrow P)\circ\Gamma$ is a quasi-compact immersion.

*Step 2: the closure.* $P$ is proper over $S$ (base change of $p_2$ along
$p_1$, followed by $p_1$), hence quasi-separated. By
[lemma-nagata-immersion-open-in-scheme-image], $\delta$ factors through its
scheme-theoretic image $Z$ as a quasi-compact open immersion $j:X\to Z$
which is scheme-theoretically dense. $Z$ is closed in $P$, so $Z\to S$ is
proper. Thus $c$ is a dense compactification, and $q_k\circ j=
\mathrm{pr}_k\circ\delta=j_k$. Each $q_k$ is an $S$-morphism.

*Step 3: inverse image of $X$.* The scheme-theoretic image of a quasi-compact
morphism commutes with restriction to opens of the target
([lemma-nagata-scheme-image-restrict-open]). Hence
$Z\cap P^\circ$ is the scheme-theoretic image of
$\Gamma:X\to P^\circ$. Since $\Gamma$ is a closed immersion, its
scheme-theoretic image is $\Gamma(X)$ itself. Therefore

$$
q_1^{-1}(j_1(X))=Z\cap\mathrm{pr}_1^{-1}(j_1(X))=Z\cap P^\circ=\Gamma(X)=j(X).
$$

The same argument with the roles of the factors exchanged gives
$q_2^{-1}(j_2(X))=j(X)$. So $q_1,q_2$ are refinements $c\to c_1$,
$c\to c_2$.

*Step 4: finite families.* For a family $c_1,\ldots,c_n$ with $n\geq1$,
argue by induction: for $n=1$ apply the construction to $c_1,c_1$ (or take
the dense refinement of $c_1$ by schematic closure); given a common dense
refinement $c'$ of $c_1,\ldots,c_{n-1}$, Steps 1–3 applied to $c',c_n$ give a
dense $c$ with refinements $c\to c'$ and $c\to c_n$, and composing $c\to c'$
with $c'\to c_k$ gives refinements $c\to c_k$, since refinements compose
([det-nagata-definition-refinement]).
