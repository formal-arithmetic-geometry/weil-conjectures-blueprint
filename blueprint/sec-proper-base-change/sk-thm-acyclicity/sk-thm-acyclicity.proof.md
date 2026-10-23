+++
kind = "proof"
of = "sk-thm-acyclicity"
+++
For the first assertion put $Z^0=F$ and let $Z^{m+1}$ be the image of
$A^m\to A^{m+1}$. The exact sequences

$$
0\longrightarrow Z^m\longrightarrow A^m\longrightarrow Z^{m+1}\longrightarrow0
$$

give

$$
\operatorname{coker}(vA^m\to vZ^{m+1})\simeq R^1vZ^m,
\qquad R^avZ^{m+1}\simeq R^{a+1}vZ^m\quad(a\geq1).
$$

Left exactness identifies the kernel of $vA^q\to vA^{q+1}$ with $vZ^q$.
Consequently, for $q\geq1$,

$$
\mathcal H^q(vA^\bullet)=\operatorname{coker}(vA^{q-1}\to vZ^q)
\simeq R^1vZ^{q-1}\simeq\cdots\simeq R^qvF,
$$

and degree zero is $vF$.

For the complex assertion first observe that a bounded below exact complex
of $v$-acyclic objects remains exact after applying $v$. Indeed, its cycle
sequences have the same form, starting with a zero cycle at the first nonzero
degree. The long exact sequences show inductively that all cycles are
$v$-acyclic, so each cycle sequence remains short exact after $v$. Now choose
a quasi-isomorphism $A^\bullet\to J^\bullet$ to a bounded below complex of
injectives. Its cone is bounded below, exact, and termwise $v$-acyclic, since
its terms are finite direct sums of terms of $A^\bullet$ and of $J^\bullet$.
Applying $v$ to the cone shows that $vA^\bullet\to vJ^\bullet$ is a
quasi-isomorphism. The target computes $Rv(A^\bullet)$, proving the
assertion. No spectral sequence is needed; this is why the lemma is separated
from [det-thm-groth-ss].
