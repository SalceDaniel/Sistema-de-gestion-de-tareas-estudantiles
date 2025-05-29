from PyQt6.QtCharts import QChartView, QChart, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis, QPieSeries
import PyQt6.QtGui


class GraficosReportes:
    def crear_grafico_circular(self, titulo: str, lista_etiquetas: list[str], lista_valores):
        # Crear datos para el diagrama de pastel
        series = QPieSeries()
        for i in range(len(lista_etiquetas)):
            series.append(lista_etiquetas[i], lista_valores[i])

        # Configurar el diagrama de pastel
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(titulo)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        # Personalizar las secciones del diagrama
        for parte in series.slices():
            parte.setLabel(f"{parte.label()} ({parte.percentage() * 100:.1f}%)")

        # Crear QChartView
        chart_view = QChartView(chart)
        chart_view.setRenderHint(PyQt6.QtGui.QPainter.RenderHint.Antialiasing)
        return chart_view
