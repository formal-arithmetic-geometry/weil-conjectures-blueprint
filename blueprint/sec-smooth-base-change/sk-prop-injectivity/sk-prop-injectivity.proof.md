+++
kind  = "proof"
of    = "sk-prop-injectivity"
+++
*Step 1 (embed in an injective).* Choose a short exact sequence
$0\to\mathcal F\to\mathcal I\to\mathcal Q\to0$ with $\mathcal I$ an
injective sheaf of $\Lambda$-modules on $T_{\Et}$. An injective object
is its own injective resolution, so $R^qg_*\mathcal I=0$ for $q>0$.

*Step 2 (compare the two long exact sequences).* The functors
$f^{-1}$ and $e^{-1}$ are exact, so applying $f^{-1}R^\bullet g_*$ to
the sequence and $R^\bullet h_*$ to its $e^{-1}$-image gives two exact
rows, and the base-change maps of [sk-def-bc] are natural, hence give
the vertical arrows of

$$
\begin{array}{ccccccc}
f^{-1}R^{q-1}g_*\mathcal I&\to&f^{-1}R^{q-1}g_*\mathcal Q&\to&
f^{-1}R^{q}g_*\mathcal F&\to&0\\
\downarrow&&\downarrow&&\downarrow&&\\
R^{q-1}h_*e^{-1}\mathcal I&\to&R^{q-1}h_*e^{-1}\mathcal Q&\to&
R^{q}h_*e^{-1}\mathcal F&\to&R^{q}h_*e^{-1}\mathcal I .
\end{array}
$$

The top right entry is $f^{-1}R^qg_*\mathcal I=0$ by Step 1, so the top
row exhibits $f^{-1}R^qg_*\mathcal F$ as the cokernel of its left map.
The two left-hand verticals are isomorphisms by
$\mathrm{BC}(f,\Lambda,q-1)$, so that cokernel is identified with the cokernel
of the bottom left map, which is the image of
$R^{q-1}h_*e^{-1}\mathcal Q\to R^qh_*e^{-1}\mathcal F$. The middle
vertical is therefore the inclusion of that image: this is (1).

*Step 3 (the cokernel).* Exactness of the bottom row continues the
identification: the quotient of $R^qh_*e^{-1}\mathcal F$ by that image
injects into $R^qh_*e^{-1}\mathcal I$, which is (3). For (2), run the
same diagram for $0\to\mathcal F\to\mathcal G\to\mathcal G/\mathcal F\to0$
with $\mathcal F\subseteq\mathcal G\subseteq\mathcal I$; the
degree-$(q-1)$ isomorphisms again give the inclusion of the cokernel for
$\mathcal F$ into the one for $\mathcal G$.

*Step 4 (a failure is a cokernel element at a point).* By (1) the
base-change map is an isomorphism if and only if its cokernel vanishes,
and a sheaf vanishes if and only if all its stalks do; so if
$\mathrm{BC}(f,\Lambda,q)$ fails there is a geometric point $\bar x$ of $X$
and an element of $(R^qh_*e^{-1}\mathcal F)_{\bar x}$ outside the image.

This is Stacks, Étale Cohomology, Lemma 59.88.2
([`0F03`](https://stacks.math.columbia.edu/tag/0F03)).
