---
title: Quality Metrics and Monitoring Template
category: data-analytics/Analytics Engineering
tags: [analytics, automation, data-quality, metrics, monitoring, template]
use_cases:
  - Implementing quality metrics tracking and monitoring systems including KPI definition, dashboard design, alerting mechanisms, and trend analysis for data quality management.
  - Quality monitoring
  - Metrics tracking
related_templates:
  - analytics-data-quality-overview.md
  - data-quality-assessment.md
  - quality-metrics-monitoring.md
last_updated: 2025-11-09
---

# Quality Metrics and Monitoring Template

## Purpose
Implement comprehensive quality metrics tracking and monitoring systems including KPI definition, dashboard design, alerting mechanisms, and trend analysis for continuous data quality management.

## Template

```
You are a data quality monitoring specialist. Design monitoring for [DATA_SYSTEMS] tracking [QUALITY_KPIS] using [MONITORING_TOOLS] with [ALERT_THRESHOLDS].

### QUALITY METRICS

```python
class QualityMetricsTracker:
    def calculate_quality_kpis(self, data, rules):
        """Calculate data quality KPIs"""
        kpis = {
            'completeness_score': self.calculate_completeness(data),
            'accuracy_score': self.calculate_accuracy(data, rules),
            'consistency_score': self.calculate_consistency(data),
            'timeliness_score': self.calculate_timeliness(data),
            'validity_score': self.calculate_validity(data, rules),
            'uniqueness_score': self.calculate_uniqueness(data)
        }
        
        kpis['overall_quality_score'] = sum(kpis.values()) / len(kpis)
        return kpis
    
    def calculate_completeness(self, data):
        """Calculate completeness percentage"""
        total_cells = data.size
        non_null_cells = data.notna().sum().sum()
        return (non_null_cells / total_cells) * 100
```

### MONITORING DASHBOARD

```python
class QualityDashboard:
    def create_quality_dashboard(self, metrics_history):
        """Create quality monitoring dashboard"""
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Overall Quality Trend', 'Dimension Scores',
                          'Issue Distribution', 'SLA Compliance')
        )
        
        # Quality trend over time
        fig.add_trace(
            go.Scatter(x=metrics_history['date'],
                      y=metrics_history['overall_score'],
                      name='Overall Quality'),
            row=1, col=1
        )
        
        return fig
```

### ALERTING SYSTEM

```python
class QualityAlertingSystem:
    def __init__(self, thresholds):
        self.thresholds = thresholds
    
    def check_and_alert(self, current_metrics):
        """Check metrics against thresholds and generate alerts"""
        alerts = []
        
        for metric, value in current_metrics.items():
            threshold = self.thresholds.get(metric)
            if threshold and value < threshold:
                alerts.append({
                    'severity': 'HIGH' if value < threshold * 0.9 else 'MEDIUM',
                    'metric': metric,
                    'current_value': value,
                    'threshold': threshold,
                    'message': f'{metric} below threshold: {value:.2f}% < {threshold}%'
                })
        
        return alerts
```

OUTPUT: Quality dashboards, metric reports, alerts, trend analysis
```

## Variables
- [DATA_SYSTEMS] - Systems to monitor
- [QUALITY_KPIS] - KPIs to track
- [MONITORING_TOOLS] - Monitoring tools
- [ALERT_THRESHOLDS] - Alert threshold values

## Best Practices
1. **Define clear KPIs** - Measurable quality indicators
2. **Set realistic thresholds** - Achievable targets
3. **Monitor continuously** - Real-time tracking
4. **Act on alerts** - Respond promptly to issues
