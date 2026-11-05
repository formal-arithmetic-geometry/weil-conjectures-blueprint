+++
id = "definition-change-of-coefficients-maps--6"
kind = "definition"
title = "Change-of-coefficients maps (6)"
name_showing = false
order = 631007
aliases = ["bp-r191-6"]
lean = ["CategoryTheory.Functor.LaxMonoidal.ihomComparison"]
uses = ["definition-change-of-coefficients-maps--3"]
+++
For $K,L\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, the map
$\cHom(K,L)_{\Lambda'}\to\cHom(K_{\Lambda'},L_{\Lambda'})$ is the
adjoint transpose, under $-\otimes^{\mathbf L}K_{\Lambda'}\dashv
  \cHom(K_{\Lambda'},-)$, of

$$
\cHom(K,L)_{\Lambda'}\otimes^{\mathbf L}_{\Lambda'}K_{\Lambda'}
\simeq\bigl(\cHom(K,L)\otimes^{\mathbf L}_\Lambda K\bigr)_{\Lambda'}
\xrightarrow{(\mathrm{ev})_{\Lambda'}}L_{\Lambda'},
$$

where the first arrow is the inverse of (3) and $\mathrm{ev}$ is evaluation.
