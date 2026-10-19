+++
kind  = "proof"
of    = "sk-lem-nagata-sketch-blowups"
uses = ["sk-lem-nagata-sketch-closure", "sk-def-nagata-admissible"]
+++
The product $\mathcal I_1\mathcal I_2$ is of finite type with
$V(\mathcal I_1\mathcal I_2)=V(\mathcal I_1)\cup V(\mathcal I_2)$, which
misses $U$. On the blow-up of $\mathcal I_1$ followed by the blow-up of the
pulled-back $\mathcal I_2$ the pullback of $\mathcal I_1\mathcal I_2$ is
invertible; conversely, on the blow-up of $\mathcal I_1\mathcal I_2$ both
factors become invertible. The universal property gives maps both ways, and
uniqueness of lifts shows they are inverse (Stacks 080A). Exchanging the two
factors gives the domination of the blow-up of $\mathcal I_2$. For a center
on the first blow-up which is not itself pulled back from $T$, the
composition assertion is the finite-type ideal calculation in Stacks 080B: it
produces a finite-type ideal on $T$ whose support is $V(\mathcal I_1)$
together with the image of the second center, hence still disjoint from $U$.

The extension assertion uses extension of finite-type quasi-coherent ideals
from a quasi-compact open, with a center still outside $U$; multiplying by a
finite-type ideal cutting out $T\setminus V$ keeps the restriction to $V$.
The precise admissible extension result is Stacks 080M. These results turn
local constructions into one global modification preserving $U$.
