+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-pushforward-extension-zero"
uses = ["def-weil-pbc-extension-by-zero", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
A natural transformation is an isomorphism as soon as all its components
are, so it suffices to show that $\beta_G=\beta_{\bar v,j_Y,G}$ is an
isomorphism for a fixed $G$. By conservativity of geometric stalks
([lemma-weil-pbc-geometric-stalk-conservative]) it suffices to check this on
the stalk at every geometric point $\bar y\to Y$ with algebraically closed
residue field.

*Points of $V$.* The restriction $j_Y^{-1}\beta_G$ is an isomorphism: by the
triangle identity for $(j_Y)_!\dashv j_Y^{-1}$, it is identified, via the
unit isomorphism $v_*G\cong j_Y^{-1}(j_Y)_!v_*G$, with the isomorphism
$v_*G\xrightarrow{\sim}j_Y^{-1}\bar v_*(j_X)_!G$ to which $\beta_G$ is
adjoint; the latter is built from the unit isomorphism of $(j_X)_!\dashv
j_X^{-1}$ and the finite base change isomorphism
([lemma-weil-pbc-finite-exchange]). If $\bar y$ factors through $V$, the
stalk of $\beta_G$ at $\bar y$ is the stalk of $j_Y^{-1}\beta_G$ at the lifted
point, hence an isomorphism.

*Points outside $V$.* If $\bar y$ does not lie in $V$, the stalk of
$(j_Y)_!v_*G$ at $\bar y$ is zero ([def-weil-pbc-extension-by-zero]). Since
the square is Cartesian, no geometric point of the finite fibre
$X\times_Y\bar y$ lies in $U$, so the pullback of $(j_X)_!G$ to this fibre
vanishes, and by finite base change the stalk of $\bar v_*(j_X)_!G$ at
$\bar y$ is zero as well. A map between zero objects is an isomorphism.
